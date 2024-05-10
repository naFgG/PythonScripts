from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject

tree = PdfReader(open('底图.pdf', 'rb'))
legend = PdfReader(open('顶图.pdf', 'rb'))
out = PdfWriter()
tree_page = tree.pages[0]
legend_page = legend.pages[0]

# 用底图的尺寸来调整顶图的尺寸
mb = tree_page.mediabox
legend_page.mediabox = RectangleObject((mb.left, mb.bottom, mb.right+3000, mb.top))
# 缩小顶图的尺寸
legend_page.scale_by(0.35)
# 顶图x轴移动
op = Transformation().translate(tx=mb.right-170)
legend_page.add_transformation(op)
tree_page.merge_page(legend_page)
out.add_page(tree_page)
with open('结果.pdf', 'wb') as outputStream:
    out.write(outputStream)
