<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize inputs
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars(trim($_POST['message'] ?? ''));

    if ($email && $name && $message) {
        $to = "yourEmail@gmail.com";
        $subject = "This is the subject line";
        $txt = "Name: $name\r\nEmail: $email\r\nMessage: $message";
        $headers = "From: noreply@demosite.com\r\n" .
                   "CC: somebodyelse@example.com";

        if (mail($to, $subject, $txt, $headers)) {
            header("Location: last.html");
            exit;
        } else {
            echo "Error: Email could not be sent.";
        }
    } else {
        echo "Invalid input. Please check your details.";
    }
}
?>
