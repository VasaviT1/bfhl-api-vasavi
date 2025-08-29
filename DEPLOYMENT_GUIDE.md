# BFHL API Deployment Guide

## Prerequisites
- Python 3.9+
- Git
- GitHub account
- Render account (free tier available)

## Local Testing

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
python main.py
```

3. **Test the API:**
```bash
python manual_test.py
```

4. **Test with HTTP requests:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R","$"]}'
```

## GitHub Deployment

1. **Initialize Git repository:**
```bash
git init
git add .
git commit -m "Initial commit: BFHL REST API"
```

2. **Create GitHub repository:**
   - Go to https://github.com/new
   - Create a new repository named `bfhl-api`
   - Don't initialize with README (we already have one)

3. **Push to GitHub:**
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bfhl-api.git
git push -u origin main
```

## Render Deployment

1. **Connect GitHub to Render:**
   - Go to https://render.com
   - Sign up/Login
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select your `bfhl-api` repository

2. **Configure the service:**
   - **Name:** `bfhl-api` (or your preferred name)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free (sufficient for testing)

3. **Deploy:**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Your API will be available at: `https://your-service-name.onrender.com`

## Testing Deployed API

Replace `YOUR_DEPLOYED_URL` with your actual Render URL:

```bash
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R","$"]}'
```

## Troubleshooting

### Common Issues:

1. **ModuleNotFoundError: No module named 'app':**
   - Fixed by using `wsgi.py` as entry point
   - Render configuration uses `gunicorn wsgi:app`

2. **Build fails on Render:**
   - Check Python version in `render.yaml`
   - Verify all dependencies in `requirements.txt`

3. **API returns 500 error:**
   - Check Render logs for detailed error messages
   - Ensure all required fields are present in response

4. **CORS issues (if testing from browser):**
   - Add Flask-CORS if needed for frontend integration

### Logs:
- View logs in Render dashboard under "Logs" tab
- Use `print()` statements for debugging (visible in logs)

## Performance Notes

- Free tier on Render may have cold starts
- For production, consider upgrading to paid tier
- API handles basic validation and error cases