# SheCab – Assisted Mobility & Safety Platform

**Mobility without limits. Assistance with heart.**

SheCab (SafeMove) is a front-end prototype of an assisted mobility platform. It combines regular ride booking with trained helpers and safety features, so elderly people, people with physical challenges, patients, and women who prioritize safety can travel with confidence.

Most ride apps only move people from A to B. SheCab treats mobility as a supportive service: users choose the level of help they need and, if they wish, the gender of their driver or helper.

---

## Demo Video

Watch the project demo here: [SheCab Demo Video](https://drive.google.com/file/d/1PsjAUXzG-psv4uMhPa9vgcbMcr7_2S85/view?usp=drivesdk)

---

## Features

- **Four service types**
  - Ride Premium: sedan, AC guaranteed, top-rated driver (₹299)
  - Ride: standard hatchback (₹149)
  - Porter: luggage and physical help (₹99)
  - On-Demand: time-based helper for short tasks (₹5/min, 1–8 hour slider)
- **Gender Preference Matching**: choose Female, Male, or No preference. If no female helper is free, the app shows a probability prediction such as *"45% chance of a female helper available in 12 minutes."*
- **Automatic fare calculation** with no surge pricing
- **Helper profile** with rating, experience, distance, and contact
- **Booking confirmation** with a 4-digit OTP
- **Live tracking** on a Leaflet map with a moving helper marker and ETA
- **Safety tools**: SOS alert, share trip link, OTP verification
- **Message helper** screen
- **Cancel booking** with a reason and a fee notice
- **Rate your helper** with stars, quick tags, and feedback
- **Trip history** ("Your trips")
- Mobile-first layout, keyboard focus styles, and screen-reader labels

---

## Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Page structure |
| CSS3 | Styling and responsive mobile layout |
| JavaScript (vanilla) | App flow, matching logic, fare calculation |
| Leaflet.js 1.9.4 | Map and live tracking |
| OpenStreetMap | Map tiles |
| VS Code + Live Server | Development and running the prototype |

---

## Project Structure

```text
shecab/
│
├── index.html      # Entire prototype (HTML + CSS + JavaScript)
└── README.md
```

---

## How to Run

1. Download or extract the project folder.
2. Open the folder in **Visual Studio Code**.
3. Right-click `index.html` and choose **Open with Live Server**.
   (You can also double-click `index.html` to open it in a browser.)
4. The app opens in your browser.

> **Internet connection required.** Leaflet and the map tiles load from the web.

---

## App Flow

| Step | Screen | What happens |
|---|---|---|
| 1 | Welcome | Get started or sign in |
| 2 | Service type | Choose Ride Premium, Porter, Ride, or On-Demand |
| 3 | Helper gender | Choose a preference and see the availability prediction |
| 4 | Booking details | See the fare, set duration (On-Demand), add pickup and notes |
| 5 | Helper profile | Review the matched helper |
| 6 | Booking confirmed | Receive the OTP |
| 7 | Live tracking | Watch the helper arrive; use SOS, Share trip, or Verify OTP |
| 8 | Message / Cancel | Chat with the helper or cancel with a reason |
| 9 | Rate your helper | Stars, tags, and feedback |
| 10 | Your trips | Completed trips and totals |

---

## How Matching Works

1. The app filters helpers who are available and match the chosen gender.
2. It sorts them by distance and assigns the nearest one.
3. If the user asks for a female helper and none are available, it estimates the chance and wait time using:
   - Density of nearby female helpers
   - Current online/offline status
   - A historical availability weight
   - The expected arrival time of the next eligible helper

In this prototype the helper list and the historical weight are demo values. A production version would replace them with live location data and availability logs.

---

## Configuration

**Change the map location.** In `index.html`, edit the `USER` constant:

```js
const USER = [17.3457, 78.5522]; // latitude, longitude
```

**Change prices.** Edit the `SERVICES` object:

```js
const SERVICES = {
  premium:  { name: "Ride Premium", fare: 299 },
  ride:     { name: "Ride", fare: 149 },
  porter:   { name: "Porter", fare: 99 },
  ondemand: { name: "On-Demand", perMin: 5, timed: true }
};
```

**Change demo helpers.** Edit the `HELPERS` array (name, gender, rating, experience, distance, availability).

**Connect a backend.** The SOS button currently logs its payload to the browser console. To send it to a server, replace the `console.log` in `sendAlert()` with:

```js
fetch("/api/send-alert/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body
});
```

---

## Prototype Limitations

- Helpers, prices, ratings, and predictions are demo data.
- No real login: "Get started" and "Sign in" go straight to the booking flow.
- Trip history is kept in memory and resets when the page is refreshed.
- The SOS alert and chat are simulated; nothing is sent to a server.
- Live tracking is an animated simulation, not real GPS.

---

## Future Enhancements

1. Backend with user authentication and a database (Django or Node.js)
2. Helper registration, verification, and certification
3. Real-time GPS tracking and live helper availability
4. Emergency alerts sent to trusted contacts with location
5. Machine learning for availability prediction (e.g., Random Forest), travel-time estimation, and safety risk scoring
6. Online payments, cost calculation, and payment history
7. Persistent booking dashboard and trip history

---

## Real-World Applications

- Elderly assistance
- Support for people with disabilities
- Women's safety
- Hospital visits
- Railway and airport assistance (luggage, platforms, boarding)
- Travel companionship
- Guidance on urban public transport
- Independent living support

---

## Project Goal

To show how technology, accessibility, and compassionate human assistance can come together to make everyday travel safer and more inclusive for everyone.

---

**Project Name:** SheCab / SafeMove
**Category:** Assisted Mobility & Safety Platform
**Frontend:** HTML, CSS, JavaScript, Leaflet.js
**Status:** Prototype
