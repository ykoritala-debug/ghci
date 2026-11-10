document.getElementById("bookingForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const tier = document.getElementById("tier").value;
  fetch("/api/book/", {
    method: "POST",
    body: JSON.stringify({
      tier: parseInt(tier),
      start_time: new Date().toISOString(),
      route: "Home to Clinic"
    }),
    headers: { "Content-Type": "application/json" }
  }).then(response => response.json()).then(data => {
    console.log("Booking ID:", data.booking_id);
  });
});