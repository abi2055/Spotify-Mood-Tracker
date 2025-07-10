## Spotify Mood Tracker

A web-based application that connects to a user's Spotify account using **OAuth 2.0** and retrieves recently played tracks to analyze emotional trends through genre classification. Built using **Flask** and Spotify’s Web API, the app securely accesses user listening data and visualizes patterns using **Matplotlib**.

### Features
- 🔐 Integrated **Spotify OAuth authentication** for secure user login and token refresh
- 📡 Pulled personal listening data from Spotify’s **Recently Played** endpoint
- 🎵 Retrieved genre information via Spotify’s **Artist API**
- 📁 Saved raw data and genre info to local `.json` and `.txt` files
- 📊 (Optional) Use `Matplotlib` to generate graphs of mood trends based on genre tags

### Performance Highlights
- ✅ Fully implemented OAuth flow with **100% secure token handling**
- 📊 Genre classification and visualization revealed **weekly emotional patterns**
- ⚙️ Built with modular Python and **object-oriented programming** principles

### 🛠️ Technologies Used

| Category               | Tools & Libraries                                      |
|------------------------|--------------------------------------------------------|
| **Language**           | Python                                                 |
| **Framework**          | Flask                                                  |
| **API Integration**    | Spotify Web API, OAuth 2.0                             |
| **HTTP Requests**      | requests                                               |
| **Data Handling**      | JSON, File I/O                                         |
| **Visualization**      | Matplotlib (for mood trend graphs)                    |
| **Hosting/Interface**  | Flask localhost (runs at `localhost:5000`)            |

### 🚀 How It Works
1. User clicks “Login with Spotify” and is redirected to the Spotify OAuth flow.
2. On success, an access token is stored and used to query recently played songs.
3. For each song, the app collects genre data via the **Artist endpoint**.
4. Genres are written to a `.txt` file and saved alongside a `.json` data dump.
5. (Optional) Visualizations can be created to track mood trends over time.

---

**Note**: Be sure to replace `CLIENT_ID`, `CLIENT_SECRET`, and `app.secret_key` with your own Spotify Developer credentials.

![Example Visualization](https://github.com/user-attachments/assets/4b8ea525-b70f-4f5c-aaa3-7ff6f7c02047)
