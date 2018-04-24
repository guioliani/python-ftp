<?php
	require("configs/connection.php");
	session_start();
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8" />
	<title>Login</title>
	<link href='http://fonts.googleapis.com/css?family=Oswald:400,300,700' rel='stylesheet' type='text/css'/>
	<link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body>
	<div class="cadastrar"><a href="cadastro.php" title="cadastre-se">Cadastre-se &raquo;</a></div>
	<div class="cadprof"><a href="index.html" title="cadastre-se">Inicio &raquo;</a></div>

	<div class="formulario" class="form bradius">
		<div class="message">

		</div>
		<div class="logo"></div>
		<div class="acomodar";>
			<form action="?acao=logar"method="POST">
				<label for="email">E-mail</label><input id="email" type="text" class="txt bradius" name="email" values=""/>
				<label for="senha">Senha</label><input id="senha" type="password" class="txt bradius" name="senha" values=""/>
				<input type="submit" id="logar" class="sb bradius" value="Entrar" name="button"/>
				<input type="submit" id="logar" class="sb bradius" value="Recuperar senha" name="recupera"/>
				
			</form>
		</div>
	</div>

	<script src="js/jquery.js"></script>
</body>
</html>

<?php
	if(isset($_POST["button"])){
		$email = mysqli_real_escape_string($mysqli, $_POST["email"]);
		$senha = mysqli_real_escape_string($mysqli, md5($_POST["senha"]));

		if($email == "" || $senha == ""){
			echo "
					<div class='aviso yellow'>
					Preencha todos os campos!!
			          </div>
			";
			return true;
		}

		//$select = $mysqli->query("SELECT * FROM usuarios_n WHERE email='$email' AND senha='$senha'");
		$select = $mysqli->query("SELECT id, nome, email, nivel, senha, status FROM usuarios_n WHERE email='$email' AND senha='$senha'
									UNION
								  SELECT id, nome, email, nivel, senha, status FROM usuarios_prof WHERE email='$email' AND senha='$senha'
								  	UNION
								  SELECT id, nome, email, nivel, senha, status FROM administrador WHERE email='$email' AND senha='$senha'");

		$row = $select->num_rows;
		$get = $select->fetch_array();

		$id =$get['id'];
		$_SESSION['id'] = $id;
 	
		$nome =$get['nome'];
		$perm = $get['nivel'];
		$status = $get['status'];

		if($row > 0){
			if($perm == 1 AND $status == 1){
				session_start();
				$_SESSION["nivel"] = 1;
				echo '
				<div class="aviso green">
						logado com sucesso!!
				</div>
				';
			sleep(2);
			header('Location: templates/nivel1.php');
		}elseif($perm == 2 AND $status == 1){
			session_start();
			$_SESSION["nivel"] = 2;
			sleep(2);
			header('Location: templates/nivel2.php');
		}elseif($perm == 3 AND $status == 1){
			session_start();
			$_SESSION["nivel"] = 3;
			sleep(2);
			header('Location: templates/admin.php');
		}else{
			echo "	<div class='aviso yellow'>
					Sua conta foi bloqueada!!
			          </div>";
		}

		}else{
			echo "	<div class='aviso yellow'>
					Usuario ou senha incorretos!!
			          </div>";
		}
	}elseif(isset($_POST['recupera'])){
		header("Location: recuperasenha.php");
	}
?>
