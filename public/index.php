<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>サンプルページ</title>
</head>
<body>
    <?php
    # unameでOS名とアーキテクチャ名を取得
    $uname = posix_uname();
    $os = $uname['sysname'];
    $arch = $uname['machine'];
    ?>
    <p>
        このページは <?= $os ?> (<?= $arch ?>) で動作しています。
    </p>
    <p>
        <a href="test.php">test.php(DB接続テスト)</a>
</body>
</html>
