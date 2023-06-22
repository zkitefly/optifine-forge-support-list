# 请输入 Minecraft 版本和 Optifine 版本
<body>
  <form>
    <label for="value1">Minecraft 版本（例如 1.20.1）</label>
    <input type="text" id="value1" name="value1" required><br><br>
    
    <label for="value2">Optifine 版本（例如 HD_U_I5_pre4）</label>
    <input type="text" id="value2" name="value2" required><br><br>
    
    <button type="button" onclick="navigate()">→点击此处查询←</button>
  </form>

  <script>
    function navigate() {
      var value1 = document.getElementById("value1").value;
      var value2 = document.getElementById("value2").value;
      
      // 构建跳转URL，这里假设使用value1和value2作为参数
      var url = "https://zkitefly.github.io/optifine-forge-support-list/versionlist/" + value1 + "-" + value2;
      
      // 跳转到目标页面
      window.location.href = url;
    }
  </script>
</body>
</html>
