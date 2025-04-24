# 🧪 Apache SSL Server

> A Docker-based practice to configure Apache with self-signed SSL certificates and serve a secure website.

---

## 🎯 Objective

Learn how to use a custom Dockerfile to create an Apache HTTPS server using self-signed certificates.

---

## 🧰 Technologies Used

- Docker
- Apache2
- OpenSSL

---

## 📂 Files & Structure

```bash
apache-ssl/
├── Dockerfile
├── docker.key
├── docker.crt
├── ssl.conf
└── html/
    └── index.html
```

---

## 📝 Steps Performed

1. Created a working directory and placed an `index.html` file inside a `html/` folder.
2. Generated a self-signed SSL certificate and private key using the following command:
   ```bash
   openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout docker.key -out docker.crt
   ```
3. Wrote a `Dockerfile` to:
   - Install Apache, PHP and SSL modules
   - Copy the HTML content and SSL certificates into the image
   - Replace the default Apache SSL config with a custom one
4. Built the Docker image using:
   ```bash
   docker build -t apache_ssl .
   ```
5. Ran the container on port 443:
   ```bash
   docker run -d --name apache_ssl -p 443:443 apache_ssl
   ```

---

## 💡 Useful Commands

```bash
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout docker.key -out docker.crt
docker build -t apache_ssl .
docker run -d --name apache_ssl -p 443:443 apache_ssl
docker stop apache_ssl
docker start apache_ssl
```

---

## ✅ Expected Result

When accessing `https://localhost` in the browser, a secure HTTPS page served by Apache from within the container should appear. The browser may show a warning due to the self-signed certificate, which is expected.

---

## 🔗 References

- [Apache SSL Configuration Guide](https://httpd.apache.org/docs/current/ssl/ssl_howto.html)
- [Docker Documentation](https://docs.docker.com/)
- [OpenSSL - Self-Signed Certificate One-Liner](https://major.io/p/generate-self-signed-certificate-and-key-in-one-line/)
