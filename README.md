# Omani Nursing Association: website prototype (Streamlit)

Bilingual (English / Arabic) website prototype, shown behind an access code.

## Files
- `app.py`: access-code page, then the full website
- `site/index.html`: the website (single self-contained file)
- `requirements.txt`, `.streamlit/config.toml`: settings for Streamlit Cloud

## Deploy on Streamlit Community Cloud
1. Create a GitHub repository (private is fine) and upload all files in this folder, keeping the folder structure.
2. Go to https://share.streamlit.io, sign in with GitHub, click **Create app**, choose the repository, branch `main`, main file `app.py`.
3. Under **Advanced settings → Secrets**, paste:
   `ACCESS_CODE = "choose-your-code"`
4. Click **Deploy**. Share the app link and the code with the ONA board.

To change the code later: App → Settings → Secrets. To update the site: replace `site/index.html` in GitHub; the app redeploys automatically.

## Run locally
```
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

© 2026 Omani Nursing Association. All rights reserved. Powered by Knowledge Horizon.
