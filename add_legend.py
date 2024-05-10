from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject

tree = PdfReader(open('graphlan_tree_1.pdf', 'rb'))
legend = PdfReader(open('legend.pdf', 'rb'))
out = PdfWriter()
tree_page = tree.pages[0]
legend_page = legend.pages[0]

mb = tree_page.mediabox
legend_page.mediabox = RectangleObject((mb.left, mb.bottom, mb.right+3000, mb.top))
legend_page.scale_by(0.35)
op = Transformation().translate(tx=mb.right-170)
legend_page.add_transformation(op)
tree_page.merge_page(legend_page)
out.add_page(tree_page)
with open('graphlan_tree.pdf', 'wb') as outputStream:
    out.write(outputStream)
