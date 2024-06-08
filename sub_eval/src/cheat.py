import cv2
import numpy as np

# Paths to YOLO files
weights_path = "D:/xampp/htdocs/AI-proctoring-exam/proctoring-main/src/yolov3.weights"
config_path = "D:/xampp/htdocs/AI-proctoring-exam/proctoring-main/src/yolov3.cfg"
names_path = "D:/xampp/htdocs/AI-proctoring-exam/proctoring-main/src/coco.names"


# Load YOLO
net = cv2.dnn.readNet(weights_path, config_path)

# Load COCO class labels
with open(names_path, "r") as f:
    classes = f.read().strip().split("\n")

# Capture video from camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Create blob from input image
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set input blob for the netwFork
    net.setInput(blob)

    # Forward pass through the network
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    # Lists to store detected bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []

    # Process each layer output
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Filter out weak predictions and detect persons and mobile phones (indices 0 and 67 in COCO dataset)
            if confidence > 0.5 and (class_id == 0 or class_id == 67):
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Calculate top-left corner of the bounding box
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Append to lists
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-max suppression to remove redundant overlapping boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

    # Draw bounding boxes and labels
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 5), font, 1, color, 2)

    # Display the output frame
    cv2.imshow("Camera", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
