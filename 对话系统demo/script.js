// 加载JSZip库
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/jszip';
document.head.appendChild(script);

// 文件选择器的事件处理函数
function handleFileSelect(event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function(event) {
    const content = event.target.result;
    const jsZip = new JSZip();

    // 读取Word文档中的内容
    jsZip.loadAsync(content).then(function(zip) {
      const docContent = zip.file("word/document.xml").async("string");

      // 将Word文档内容转换为HTML格式
      docContent.then(function(content) {
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(content, "text/xml");
        const elements = xmlDoc.getElementsByTagName("w:t");
        let htmlContent = "";

        for (let i = 0; i < elements.length; i++) {
          const text = elements[i].textContent;
          htmlContent += text;
          if (i < elements.length - 1) {
            htmlContent += "<br/>";
          }
        }

        // 将转换后的HTML内容显示在页面上
        document.getElementById('wordContent').innerHTML = htmlContent;
      });
    });
  };
  reader.readAsArrayBuffer(file);
}

document.getElementById('fileInput').addEventListener('change', handleFileSelect, false);
