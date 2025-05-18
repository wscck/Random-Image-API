📌 Random Image API (cwkcck/random-image-api)
一个轻量级的 随机图片 API，基于 Flask 和 Docker，支持多种格式图片的随机返回，并通过挂载方式存储图片，便于维护。

🚀 快速启动
docker run -d -p 5000:5000 -v /images:/app/images cwkcck/random-image-api

📌 参数说明

-d：后台运行容器

-p 5000:5000：映射端口，主机 5000 → 容器 5000

-v /images:/app/images：将宿主机 /images/ 目录挂载到容器 /app/images/（后者不可修改）

🌍 API 访问
运行后，直接访问：

http://lo📌 Random Image API (cwkcck/random-image-api)
一个轻量级的 随机图片 API，基于 Flask 和 Docker，支持多种格式图片的随机返回，并通过挂载方式存储图片，便于维护。

🚀 快速启动
docker run -d -p 5000:5000 -v /images:/app/images cwkcck/random-image-api

📌 参数说明

-d：后台运行容器

-p 5000:5000：映射端口，主机 5000 → 容器 5000

-v /images:/app/images：将宿主机 /images/ 目录挂载到容器 /app/images/（后者不可修改）

🌍 API 访问
运行后，直接访问：

http://localhost:5000
无需额外 URL，API 会随机返回 /images/ 目录里的图片。

🖼️ 支持的图片格式
✅ JPG / JPEG / PNG / WEBP / GIF / BMP / TIFF 任何支持的格式都可以直接存放在 /images/ 目录，API 会自动识别并返回。

🔧 适用场景
🔹 随机图片展示 API 🔹 简单图片存储方案（无需数据库） 🔹 Docker 轻量级部署，可用于本地或服务器环境
