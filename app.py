import streamlit as st
from main import encode, decode, SPACE

st.set_page_config(
    page_title="Cipher X | تشفير النصوص",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Outfit:wght@300;600&display=swap');

    /* خلفية التطبيق العامة */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #ffffff, #f0f0f0, #ffffff); /* الأسود أصبح أبيض */
        font-family: 'Outfit', 'Cairo', sans-serif;
        color: #1a1c29; /* النص يصبح داكن على الأبيض */
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
    }

    h1 {
        background: linear-gradient(to right, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
        text-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }
    
    .subtitle {
        text-align: center;
        color: #555; /* أكثر وضوح على الخلفية الفاتحة */
        font-size: 1.1rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.8); /* أبيض شفاف */
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 0, 0, 0.08);
        padding: 20px;
        margin-bottom: 20px;
    }

    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.9) !important; /* خلفية بيضاء */
        color: #000 !important; /* نص أسود */
        border: 1px solid #ccc !important;
        border-radius: 12px !important;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #b38728 !important;
        box-shadow: 0 0 10px rgba(179, 135, 40, 0.2);
    }

    div[role="radiogroup"] {
        background: rgba(255, 255, 255, 0.7); /* خلفية بيضاء شفاف */
        padding: 5px;
        border-radius: 12px;
        display: flex;
        justify-content: center;
    }

    input[type="number"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #000 !important;
        border-radius: 8px !important;
        border: 1px solid #ccc !important;
        text-align: center;
    }

    button[kind="primary"] {
        background: linear-gradient(90deg, #1cb5e0 0%, #000851 100%);
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        color: white;
        font-weight: 600;
        letter-spacing: 1px;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 100%;
        margin-top: 10px;
    }
    
    button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(28, 181, 224, 0.3);
    }

    .stAlert {
        border-radius: 10px;
        background-color: rgba(28, 181, 224, 0.1);
        border: 1px solid rgba(28, 181, 224, 0.2);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>

""", unsafe_allow_html=True)

st.markdown("<h1>CIPHER X</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Simple • Reversible • Educational</div>", unsafe_allow_html=True)


st.markdown('<div class="glass-card">', unsafe_allow_html=True)

c1, c2 = st.columns([2, 1])

with c1:
    
    mode = st.radio(
        "Select Operation / العملية",
        ["🔒 Encode (تشفير)", "🔓 Decode (فك تشفير)"],
        horizontal=True,
        label_visibility="collapsed"
    )

with c2:
    key = st.number_input(
        "Security Key (الـمـفـتـاح)",
        min_value=1,
        value=5,
        step=1,
        help="رقم الإزاحة المستخدم في التشفير"
    )

st.markdown('</div>', unsafe_allow_html=True)



clean_mode = "Encode" if "Encode" in mode else "Decode"


st.markdown(f"### {'📝 Input Text' if clean_mode == 'Encode' else '🔐 Encrypted Input'}")

input_text = st.text_area(
    label="Input",
    placeholder="Enter your text here..." if clean_mode == "Encode" else "Paste the cipher text here...",
    height=150,
    label_visibility="collapsed"
)


if st.button(f"⚡ RUN {clean_mode.upper()}", type="primary"):
    if not input_text.strip():
        st.warning("⚠️ Please enter text first | الرجاء إدخال نص")
    else:
        try:
          
            if clean_mode == "Encode":
                result = encode(input_text, key, SPACE)
                st.success("✅ Encryption Successful")
                output_label = "Encoded Result"
            else:
                result = decode(input_text, key, SPACE)
                st.success("✅ Decryption Successful")
                output_label = "Decoded Result"

            
            st.markdown("---")
            st.markdown(f"### 📤 {output_label}")
            st.code(result, language=None) 
            
        except ValueError as e:
            st.error(f"❌ An error occurred: {e}")


st.markdown("---")
st.caption(f"<div style='text-align:center; opacity:0.5'>System config: SPACE={SPACE} | Key={key}</div>", unsafe_allow_html=True)