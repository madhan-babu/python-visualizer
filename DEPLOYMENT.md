# 🚀 Deployment Guide

This guide provides detailed instructions for deploying the Python Visualizer to various platforms.

## 📋 Pre-Deployment Checklist

- [ ] All dependencies listed in `requirements.txt`
- [ ] Application runs locally without errors
- [ ] `.gitignore` properly configured
- [ ] README.md is up to date

## 🌟 Streamlit Community Cloud (Easiest & Free)

### Prerequisites
- GitHub account
- Code pushed to GitHub repository

### Steps

1. **Prepare Repository**
   ```bash
   cd /Users/rsmadhan/Documents/Repos/Python-Visualizer
   git init
   git add .
   git commit -m "Initial commit - Python Visualizer"
   ```

2. **Push to GitHub**
   ```bash
   # Create a new repository on GitHub first, then:
   git remote add origin https://github.com/YOUR_USERNAME/python-visualizer.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Main file path: `app.py`
   - Click "Deploy"
   - Wait 2-3 minutes for deployment

4. **Your App is Live!**
   - URL format: `https://YOUR_USERNAME-python-visualizer-app-xxxxx.streamlit.app`
   - Share this URL with students!

### Configuration (Optional)
Create `.streamlit/secrets.toml` for any API keys or secrets (not needed for this app).

---

## 🐳 Docker Deployment

### Prerequisites
- Docker installed
- Docker Hub account (for sharing images)

### Steps

1. **Build Docker Image**
   ```bash
   cd /Users/rsmadhan/Documents/Repos/Python-Visualizer
   docker build -t python-visualizer:latest .
   ```

2. **Test Locally**
   ```bash
   docker run -p 8501:8501 python-visualizer:latest
   ```
   Open http://localhost:8501

3. **Push to Docker Hub** (Optional)
   ```bash
   docker tag python-visualizer:latest YOUR_USERNAME/python-visualizer:latest
   docker push YOUR_USERNAME/python-visualizer:latest
   ```

4. **Run on Any Server**
   ```bash
   docker pull YOUR_USERNAME/python-visualizer:latest
   docker run -d -p 8501:8501 python-visualizer:latest
   ```

---

## 🔴 Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create Heroku App**
   ```bash
   cd /Users/rsmadhan/Documents/Repos/Python-Visualizer
   heroku create python-visualizer-app
   ```

3. **Deploy**
   ```bash
   git init  # if not already initialized
   git add .
   git commit -m "Deploy to Heroku"
   heroku git:remote -a python-visualizer-app
   git push heroku main
   ```

4. **Open App**
   ```bash
   heroku open
   ```

5. **View Logs** (if issues)
   ```bash
   heroku logs --tail
   ```

### Important Files for Heroku
- `Procfile` ✅ (already included)
- `requirements.txt` ✅ (already included)

---

## ☁️ AWS EC2 Deployment

### Prerequisites
- AWS account
- EC2 instance (t2.micro is sufficient)
- Security group allowing port 8501

### Steps

1. **Connect to EC2**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

2. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip
   ```

3. **Copy Files**
   ```bash
   # On your local machine:
   scp -i your-key.pem -r /Users/rsmadhan/Documents/Repos/Python-Visualizer ubuntu@your-ec2-ip:~/
   ```

4. **Run Application**
   ```bash
   cd ~/Python-Visualizer
   pip3 install -r requirements.txt
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```

5. **Run in Background** (Optional)
   ```bash
   nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
   ```

6. **Access**
   Open `http://your-ec2-ip:8501`

---

## 🌐 Google Cloud Run

### Prerequisites
- Google Cloud account
- gcloud CLI installed

### Steps

1. **Enable Cloud Run API**
   ```bash
   gcloud services enable run.googleapis.com
   ```

2. **Build Container**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/python-visualizer
   ```

3. **Deploy**
   ```bash
   gcloud run deploy python-visualizer \
     --image gcr.io/YOUR_PROJECT_ID/python-visualizer \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

4. **Access**
   URL will be provided after deployment

---

## 🔵 Azure Web Apps

### Prerequisites
- Azure account
- Azure CLI installed

### Steps

1. **Login**
   ```bash
   az login
   ```

2. **Create Resource Group**
   ```bash
   az group create --name PythonVisualizerRG --location eastus
   ```

3. **Create App Service Plan**
   ```bash
   az appservice plan create --name PythonVisualizerPlan \
     --resource-group PythonVisualizerRG \
     --sku B1 --is-linux
   ```

4. **Create Web App**
   ```bash
   az webapp create --resource-group PythonVisualizerRG \
     --plan PythonVisualizerPlan \
     --name python-visualizer-app \
     --runtime "PYTHON|3.9"
   ```

5. **Deploy Code**
   ```bash
   az webapp up --name python-visualizer-app \
     --resource-group PythonVisualizerRG
   ```

---

## 🛡️ Security Considerations

### For Production Deployment

1. **HTTPS**: Always use HTTPS in production
   - Streamlit Cloud: Automatic ✅
   - Heroku: Automatic ✅
   - Others: Configure SSL certificate

2. **Environment Variables**
   - Store secrets in environment variables
   - Never commit `.env` files

3. **Rate Limiting**
   - Consider adding rate limiting for public deployments
   - Use services like Cloudflare

4. **Authentication** (if needed)
   - Add Streamlit authentication
   - Or use OAuth providers

---

## 📊 Monitoring

### Recommended Tools

1. **Uptime Monitoring**
   - UptimeRobot
   - Pingdom
   - StatusCake

2. **Analytics**
   - Google Analytics (add to Streamlit app)
   - Mixpanel

3. **Error Tracking**
   - Sentry
   - Rollbar

---

## 💰 Cost Comparison

| Platform | Free Tier | Paid Tier | Best For |
|----------|-----------|-----------|----------|
| **Streamlit Cloud** | 1 private, unlimited public apps | $20/month | Quick deployment |
| **Heroku** | 550 hours/month | $7/month | Small apps |
| **AWS EC2** | 750 hours/month (12 months) | $5+/month | Full control |
| **Google Cloud Run** | 2M requests/month | Pay per use | Scalability |
| **Azure** | $200 credit | Varies | Enterprise |
| **Docker** | Free | Hosting costs | Portability |

---

## 🎓 Recommended for Educational Use

**Top Choice: Streamlit Community Cloud**
- ✅ Free forever for public repos
- ✅ Easy to deploy
- ✅ Automatic updates
- ✅ Good performance
- ✅ No server management

**Alternative: Docker on School Server**
- ✅ Full control
- ✅ No internet dependency (once deployed)
- ✅ Can run offline
- ⚠️ Requires IT support

---

## 🆘 Troubleshooting

### Deployment Fails

1. **Check logs**
   ```bash
   # Streamlit Cloud: Check dashboard
   # Heroku: heroku logs --tail
   # Docker: docker logs CONTAINER_ID
   ```

2. **Common Issues**
   - Missing dependencies → Update `requirements.txt`
   - Port conflicts → Check port configuration
   - Memory limits → Upgrade plan or optimize code

### App is Slow

1. **Solutions**
   - Enable caching with `@st.cache_data`
   - Optimize heavy computations
   - Upgrade hosting plan
   - Use CDN for static assets

---

## 📞 Support

For deployment issues:
1. Check platform-specific documentation
2. Review error logs
3. Consult community forums
4. Open GitHub issue

---

**Happy Deploying! 🚀**

