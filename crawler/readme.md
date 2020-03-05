# Crawler

> 作者：W4YNELEE

### 此資料夾內容物含以下兩種：

## 1.
```
crawler.py
```

* 此程式針對`ck101.com`或` 碩博網`擷取認證碼

```python
#碩博網
mission = Ntltd_verify_code_crawler()
mission.get_the_code2(2) #input要爬的數量
```

```python
#ck101網
mission = Ck101_verify_code_crawler()
mission.get_the_code(3) #input要爬的數量
```

***

## 2.

```
google_picture_crawler.ipynb
```

* 此程式會針對要找的圖片建立路徑且從google爬圖存取
* 將關鍵字鍵入`keyword.txt`，預設是cat
* 用Jupiter notebook開啟`google_picture_crawler.ipynb`
* Cell->run all
* 底下用Matplotlib驗證


![圖片](img1.png "result")
