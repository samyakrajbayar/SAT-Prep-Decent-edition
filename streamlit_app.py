import streamlit as st
import json
from utils import load_json, save_json, merge_dataset

st.title("SAT Oman Prep App")

menu = st.sidebar.radio("Menu", ["Quiz", "Dataset Manager"])

if menu == "Quiz":
    pyqs = load_json("data/pyqs.json")
    if not pyqs:
        st.warning("No dataset loaded.")
    else:
        lang = st.radio("Language", ["English", "Arabic"])
        q = st.selectbox("Choose a question", pyqs, format_func=lambda q: f"{q['id']} - {q['question_en']}")
        if lang == "English":
            st.write(q["question_en"])
            for i, choice in enumerate(q["choices_en"]):
                st.write(f"{i+1}. {choice}")
        else:
            st.write(q["question_ar"])
            for i, choice in enumerate(q["choices_ar"]):
                st.write(f"{i+1}. {choice}")
        ans = st.number_input("Your choice (1-4)", min_value=1, max_value=4, step=1)
        if st.button("Check"):
            if (ans-1) == q["answer_index"]:
                st.success("Correct!" if lang=="English" else "صحيح!")
            else:
                if lang=="English":
                    st.error(f"Wrong. Correct: {q['choices_en'][q['answer_index']]}")
                else:
                    st.error(f"خطأ. الصحيح: {q['choices_ar'][q['answer_index']]}")

else:
    st.header("Dataset Manager")
    option = st.radio("Choose action", ["Use existing", "Upload new", "Add to dataset", "Reset to empty", "Reset to sample"])
    if option == "Use existing":
        pyqs = load_json("data/pyqs.json")
        st.write(f"Loaded {len(pyqs)} questions.")
        st.dataframe([{"id": q["id"], "en": q["question_en"], "ar": q["question_ar"]} for q in pyqs])
    elif option in ["Upload new", "Add to dataset"]:
        uploaded = st.file_uploader("Upload JSON file", type="json")
        if uploaded:
            new = json.load(uploaded)
            if not isinstance(new, list):
                st.error("File must be a list of questions.")
            else:
                existing = load_json("data/pyqs.json")
                if option == "Upload new":
                    save_json("data/pyqs.json", new)
                    st.success(f"Replaced dataset with {len(new)} items.")
                else:
                    merged, added = merge_dataset(existing, new)
                    save_json("data/pyqs.json", merged)
                    st.success(f"Added {added} new items, total {len(merged)}.")
    elif option == "Reset to empty":
        save_json("data/pyqs.json", [])
        st.success("Dataset reset to empty.")
    elif option == "Reset to sample":
        sample = load_json("data/sample_pyqs.json")
        save_json("data/pyqs.json", sample)
        st.success("Dataset reset to sample.")
