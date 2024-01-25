function validateForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username === "admin" && password === "spi") {
    alert("Login successful!");
    window.location.href = baseUrl;  // Use the base URL defined in the HTML template
    return false;
  } else {
    alert("Invalid username or password. Please try again.");
    return false;
  }
}
