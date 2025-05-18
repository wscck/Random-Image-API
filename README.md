# 📌 Random Image API (cwkcck/random-image-api)

一个轻量级的随机图片 API，基于 **Flask** 和 **Docker**，支持多种格式图片的随机返回，并通过挂载方式存储图片，便于维护。

---

## 🚀 部署

### **克隆仓库**
```bash
git clone https://github.com/wscck/Random-Image-API.git
cd Random-Image-API
```

### **构建 Docker 镜像**
```bash
docker build -t random-image-api .
```

### **运行容器（挂载宿主机存储）**
```bash
docker run -d -p 5000:5000 -v /images:/app/images random-image-api
```

---

## 🚀 快速启动

如果您希望直接从 **Docker Hub** 拉取并运行：
```bash
docker run -d -p 5000:5000 -v /images:/app/images cwkcck/random-image-api
```

Docker Hub 地址: [cwkcck/random-image-api](https://hub.docker.com/r/cwkcck/random-image-api)

---

## 📌 参数说明

| 参数 | 说明 |
|------|------|
| `-d` | 后台运行容器 |
| `-p 5000:5000` | 映射端口，主机 `5000 → 容器 5000` |
| `-v /images:/app/images` | 挂载宿主机 `/images/` 目录至容器 `/app/images/`（后者不可修改） |

---

## 🌍 API 访问

容器运行后，可直接访问：
```
http://localhost:5000
```

### **返回随机图片**
访问 `http://localhost:5000/random`，API 会自动识别 `/images/` 目录中的图片并随机返回。

---

## 🖼️ 支持的图片格式

✅ **JPG / JPEG / PNG / WEBP / GIF / BMP / TIFF**

所有支持的格式都可直接存放在 `/images/` 目录，API 会自动识别并返回。

---

## 🔧 适用场景

🔹 **随机图片展示 API**  
🔹 **简单图片存储方案（无需数据库）**  
🔹 **Docker 轻量级部署，可用于本地或服务器环境**  

---
