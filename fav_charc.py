import streamlit as st
import ollama
import time
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Hinata Shoyo 🏐", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Remove default background so video shows */
.stApp {
    background: transparent;
    color: white;
    font-family: Arial, sans-serif;
}

/* Fullscreen Video Background */
video#bg-video {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 100vw;
    height: 100vh;
    transform: translate(-50%, -50%);
    object-fit: contain;
    background: black;
    z-index: -2;
}

/* Dark overlay */
.video-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.65);
    z-index: -1;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff7a00, #111);
    color: white;
}

/* Input Box Fixed */
div.stTextInput {
    position: fixed;
    bottom: 20px;
    left: 25%;
    width: 50%;
    z-index: 999;
}

div.stTextInput > div > div > input {
    background-color: #1e1e1e;
    color: white;
    border-radius: 12px;
    padding: 10px;
    border: 2px solid #ff7a00;
}

/* Message Box */
.message-box {
    background: rgba(0, 0, 0, 0.7);
    padding: 15px;
    border-radius: 15px;
    margin-top: 10px;
    border: 2px solid #ff7a00;
    box-shadow: 0 0 12px rgba(255,122,0,0.5);
}

/* Toss Ball */
.throw-ball {
    font-size: 70px;
    position: fixed;
    bottom: 120px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    animation: throwArc 1.8s ease-in-out forwards;
}

/* Toss Arc */
@keyframes throwArc {
    0% { transform: translate(-50%, 0px) rotate(0deg); }
    25% { transform: translate(-20%, -80px) rotate(90deg); }
    50% { transform: translate(0%, -160px) rotate(180deg); }
    75% { transform: translate(20%, -120px) rotate(270deg); }
    100% { transform: translate(40%, -200px) rotate(360deg); }
}

/* Rolling Loader */
.roll-ball {
    font-size: 60px;
    position: fixed;
    bottom: 100px;
    left: -100px;
    z-index: 1000;
    animation: rollAcross 2s linear infinite;
}

/* Faster roll for special move */
.roll-ball-fast {
    font-size: 60px;
    position: fixed;
    bottom: 100px;
    left: -100px;
    z-index: 1000;
    animation: rollAcross 1s linear infinite;
}

@keyframes rollAcross {
    0% { left: -100px; transform: rotate(0deg); }
    100% { left: 110%; transform: rotate(720deg); }
}

/* Orange Flash */
.flash-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: orange;
    z-index: 9999;
    animation: flashFade 0.8s ease-out forwards;
    pointer-events: none;
}

@keyframes flashFade {
    0% { opacity: 0.9; }
    100% { opacity: 0; }
}

/* NEW: FULL WHITE SCREEN FLASH */
.white-flash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: white;
    z-index: 10000;
    animation: whiteFade 2s ease forwards;
    pointer-events: none;
}

@keyframes whiteFade {
    0% { opacity: 1; }
    80% { opacity: 1; }
    100% { opacity: 0; }
}

/* Special Reply Styling */
.special-reply {
    background: linear-gradient(90deg, orange, red);
    color: white;
    padding: 20px;
    border-radius: 20px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    box-shadow: 0 0 25px orange;
}

</style>
""", unsafe_allow_html=True)

# ---------------- VIDEO BACKGROUND ----------------
def get_base64_video(video_file):
    with open(video_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_base64 = get_base64_video("haikyuu.mp4")

st.markdown(f"""
<div class="video-overlay"></div>
<video autoplay muted loop id="bg-video">
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Karasuno_High_School_Logo.png/512px-Karasuno_High_School_Logo.png", width=120)
    st.title("Karasuno Locker Room 🏐")
    st.markdown("Hinata Mode: ON 🔥")
    st.markdown("Energy Level: MAXIMUM")
    st.markdown("---")
    if st.button("Clear Chat"):
        st.session_state.messages = [{
            "role": "system",
            "content": """
            You are Hinata Shoyo from Haikyuu.
            You are energetic, cheerful, dramatic and obsessed with volleyball.
            Speak excitedly.
            Use volleyball metaphors.
            Encourage the user like a teammate.
            Never break character.
            """
        }]
        st.session_state.input_key = 0
        st.rerun()

# ---------------- TITLE ----------------
st.title("🏐 Hinata Shoyo Chatbot")
st.markdown("### Karasuno AI Teammate 🔥")

# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": """
        You are Hinata Shoyo from Haikyuu.
        You are energetic, cheerful, dramatic and obsessed with volleyball.
        Speak excitedly.
        Use volleyball metaphors.
        Encourage the user like a teammate.
        Never break character.
        """
    }]

# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"<div class='message-box'><b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='message-box'><b>🏐 Hinata:</b> {msg['content']}</div>", unsafe_allow_html=True)

# ---------------- USER INPUT ----------------
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

user_input = st.text_input(
    "Talk to Hinata:",
    key=f"user_input_{st.session_state.input_key}"
)

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    special_move = user_input.strip().lower() == "quick attack"

    # NEW WHITE FLASH BEFORE EVERYTHING
    if special_move:
        white_flash = st.empty()
        white_flash.markdown("<div class='white-flash'></div>", unsafe_allow_html=True)
        time.sleep(2)

    # Existing Orange Flash
    if special_move:
        flash = st.empty()
        flash.markdown("<div class='flash-screen'></div>", unsafe_allow_html=True)
        time.sleep(0.8)

    throw_placeholder = st.empty()
    throw_placeholder.markdown("<div class='throw-ball'>🏐</div>", unsafe_allow_html=True)
    time.sleep(1.8)
    throw_placeholder.empty()

    roll_placeholder = st.empty()
    if special_move:
        roll_placeholder.markdown("<div class='roll-ball-fast'>🏐</div>", unsafe_allow_html=True)
    else:
        roll_placeholder.markdown("<div class='roll-ball'>🏐</div>", unsafe_allow_html=True)

    time.sleep(1)

    response = ollama.chat(
        model="gemma3:1b",
        messages=st.session_state.messages
    )

    roll_placeholder.empty()

    reply = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

    if special_move:
        st.markdown(
            f"<div class='special-reply'>⚡ QUICK ATTACK ACTIVATED ⚡<br><br>{reply}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='message-box'><b>🏐 Hinata:</b> {reply}</div>",
            unsafe_allow_html=True
        )

    st.success("SPIKE!!! 💥")

    st.session_state.input_key += 1
    st.rerun()
