# Tumor Check

This project is a **Brain Tumor Detection Web App** built using **Flask (Python Backend) and React (Frontend)**. It allows users to upload MRI images and classify them into four categories: `glioma`, `meningioma`, `notumor`, and `pituitary`.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine after cloning from GitHub.

### **1️⃣ Clone the Repository**

```sh
# Clone the GitHub repository
git clone https://github.com/Muhammednasrudeenm/tumorCheck_project.git
cd tumorCheck_project
```

---

### **2️⃣ Create a Virtual Environment**
Since the `venv/` folder is not included in the repository, you must recreate it manually.

```sh
python -m venv backend/venv
```

---

### **3️⃣ Activate the Virtual Environment**
- **Windows (CMD/PowerShell):**
  ```sh
  backend\venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source backend/venv/bin/activate
  ```

---

### **4️⃣ Install Dependencies**
All required Python packages are listed in `requirements.txt`. Install them with:

```sh
pip install -r requirements.txt
```

---

### **5️⃣ Download the Model (`.h5` File)**
Since `.h5` model files are too large for GitHub, they are not included in the repository. The Flask app will automatically download the model when it runs.

```python
FILE_ID = "1DdZcp5DruoPU2T9ZdH34c37dYBvn9K9k" 
MODEL_PATH = "brain_tumor_model.h5"

if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
    response = requests.get(url)
    with open(MODEL_PATH, "wb") as file:
        file.write(response.content)
    print("✅ Model downloaded successfully.")
```

Ensure this code exists in your Flask app to automatically download the model when required.

---

### **6️⃣ Run the Flask Backend**
After setting up everything, start the Flask backend:

```sh
python backend/app.py
```

---

## 📌 Notes
- Ensure `venv/` is added to `.gitignore` to avoid committing unnecessary files.
- The frontend (React) setup is not included in this guide; ensure it is configured separately.

Now your project is ready to run! 🎯🚀

