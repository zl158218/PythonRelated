# PDF 转 PNG、JPG

## Code
```
import fitz

# 使用二进制打开
pdf = fitz.open("pdf", pdf_file.content)

# 使用文件名打开
# pdf = fitz.open(fname)

# 每个尺寸缩进比例
zoom_x = 2.0  # horizontal zoom
zomm_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zomm_y)

for ind, page enumerate(pdf):
    # 使用 'mat' 代替单位矩阵
    pix = page.getPixmap(matrix=mat)

    # 使用二进制保存文件
    with open(f"{ind}.png", 'wb') as f:
        f.write(pix.getImageData())
    
    # 使用自带方法保存文件
    pix.writeImage("%s.png" % ind)

```

>
> [官方文档](https://pymupdf.readthedocs.io/en/latest/faq.html#images)
> 