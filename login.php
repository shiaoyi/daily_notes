<!-- login部分 -->
<?php
if(isset($_POST['username']) && isset($_POST['password'])){
    $username = $_POST['username'];
    $password = $_POST['password'];
    if($username === 'admin' && $password === 'admin'){
?>
        <h1>登入成功！<? echo $username ?></h1>
<?php
    }else{
?>
        <h1>登入失敗！</h1>
<?php
        // 如果是要把login跟index頁面分離，可以登入失敗就跳回index，也就是轉址的動作
        // header('Location: index.php');
    }
}
?>

<!-- index部分 -->
<form action='/huli/index.php' method='POST'>
    username: <input name='username'/>
    password: <input name='password'/>
    <input type='submit'/>
</form>