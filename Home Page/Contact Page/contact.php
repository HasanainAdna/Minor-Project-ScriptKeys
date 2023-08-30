<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Retrieve form values
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  // Set up email parameters
  $to = 'textomger@gmail.com'; // Replace with the website owner's email address
  $subject = 'ScriptKeys';
  $headers = 'From: ' . $email . "\r\n" .
             'Reply-To: ' . $email . "\r\n" .
             'X-Mailer: PHP/' . phpversion();

  // Compose the email message
  $emailContent = "Name: $name\n\n";
  $emailContent .= "Email: $email\n\n";
  $emailContent .= "Message:\n$message";

  // Send the email
  if (mail($to, $subject, $emailContent, $headers)) {
    echo 'Thank you for contacting us. We will get back to you soon.';
  } else {
    echo 'Sorry, there was an error sending your message. Please try again later.';
  }
}
?>
