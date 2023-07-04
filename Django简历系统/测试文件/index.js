const fileInput = document.getElementById('file-input');
const convertBtn = document.getElementById('convert-btn');

convertBtn.addEventListener('click', async () => {
  const file = fileInput.files[0];
  if (!file) {
    alert('请上传文件');
    return;
  }
  const fileReader = new FileReader();
  fileReader.readAsText(file, 'UTF-8');
  fileReader.onload = function (e) {
    const htmlContent = e.target.result;
    const docxOutput = htmlToDocx(htmlContent);
    const fileName = file.name.replace('.html', '') + '.docx';
    saveAs(docxOutput, fileName);
  };
});

function htmlToDocx(htmlContent) {
  // 去除 HTML 中的 <!doctype> 和 <html> 标签
  const bodyContent = htmlContent
    .replace(/<!doctype[^>]*>/gi, '')
    .replace(/<\/?html[^>]*>/gi, '');
  const doc = document.implementation.createHTMLDocument();
  doc.body.innerHTML = bodyContent;

  // 将 HTML 转换为 XML（使用 DOMParser 对象实现）
  const xmlSerializer = new XMLSerializer();
  const xmlContent = xmlSerializer.serializeToString(doc);

  // 使用 html-docx-js 库将 XML 转换为 Word 文档
  return htmlDocx.asBlob(xmlContent);
}
