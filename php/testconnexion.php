<?php

    require_once("ripcord/ripcord.php");

    $url = "http://web:8069";
    $db = "odoo18";
    $username = "apiwordpress@admin.fr";
    $cleapi = "29614bbebae38294ebac1f68f03312b85cb79d09";

    $common = ripcord::client($url."/xmlrpc/2/common");

    $uid = $common->authenticate($db, $username, $cleapi, array());
    if (!empty($uid)) {
        echo "<p>Je suis connecté avec l'id : ".$uid."</p>";
    }
    else {
        echo "Impossible de me connecter";
    }
