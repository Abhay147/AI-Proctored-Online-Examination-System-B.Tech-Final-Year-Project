<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer Science Quiz with Proctoring</title>
    <style>
        /* Your CSS styles here */
    </style>
</head>

<body>
    <div class="container">
        <h1>Computer Science Quiz</h1>
        <!-- Questions and options -->
        <div class="question">
            <p>1. What does CSS stand for?</p>
            <div class="options">
                <!-- Options for question 1 -->
            </div>
        </div>
        <!-- More questions... -->
        <!-- Proctoring camera feed container -->
        <div class="proctoring-container">
            <h2>Proctoring Camera Feed</h2>
            <video id="proctoring-video" autoplay></video>
        </div>

        <?php
        // URL of the Flask API endpoint
        $url = 'http://127.0.0.1:5000/plot_data';
        
        // Fetch data from the Flask API
        $response = file_get_contents($url);
        
        // Output the response from the Flask API
        echo "<p>Data from Flask API: $response</p>";
        ?>
    </div>

    <!-- JavaScript code to access the webcam and display the feed -->
    <script>
        // Access the webcam and display the feed in the <video> element
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                var videoElement = document.getElementById('proctoring-video');
                videoElement.srcObject = stream;
            })
            .catch(function(err) {
                console.error('Error accessing the webcam: ', err);
            });
    </script>
</body>

</html>
