

`YorkuCourseSpider`  first collects all the links to the programs and then scraps specified 

items from each URL.

---

| user  | pass       | can access                      | role         |
| ----- | ---------- | ------------------------------- | ------------ |
| xxx4  | password98 | /university/                    | staff        |
| zzz3  | password98 | /                               | regular user |
| admin | 1234       | /university/< name university>/ | superuser    |
login API = /auth/jwt/create/

---

for installing the packages:
`pip install -r requirements.txt`

running tests :
`pytest`

running Scrapy by command 
```
cd crawler
scrapy crawl courses -O j.json
```

