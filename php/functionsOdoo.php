<?php
require_once('ripcord/ripcord.php');

//Connexion
$url = "http://web:8069";
$db = "odoo18";
$username = "apiwordpress@admin.fr";
$cleapi = "29614bbebae38294ebac1f68f03312b85cb79d09";


//Création du client XML-RPC à l'adresse de l'API qui permet de se connecter
$common = ripcord::client($url . "/xmlrpc/2/common");


//Appel de la méthode authenticate qui permet de se connecter à l'API
$uid = $common->authenticate($db, $username, $cleapi, array());

$object = ripcord::client("$url/xmlrpc/2/object");
function search($object, $db, $cleapi, $uid)
{
    $domain = [
        '|',
        ['state', '=', 'usable'],
        ['state', '=', 'broken'],
    ];
    $offset = 0;
    $limit = Null;
    $order = 'date_purchased desc';
    $keyword_argument = ['offset' => $offset, 'limit' => $limit, 'order' => $order, 'domain' => $domain];
    $positionnal_argument = [];

    //Appel de méthode execute_kw et affichage du résultat
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'search', $positionnal_argument, $keyword_argument);
    echo "<pre>" . print_r($donneesrecues, true) . "</pre>";
}

function search_count($object, $uid, $cleapi, $db)
{
    $domain = [
        ['age_vehicle', '>', '1'],
        ['state', '!=', 'broken'],
    ];

    $limit = Null;
    $keyword_argument = ['limit' => $limit, 'domain' => $domain];
    $positionnal_argument = [];

    //Appel de méthode execute_kw et affichage du résultat
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'search_count', $positionnal_argument, $keyword_argument);
    echo "<pre> Nombre de véhicules de plus d'1 an et qui ne sont pas cassé : " . print_r($donneesrecues, true) . "</pre>";
}

function search_read($object, $uid, $cleapi, $db)
{
    $domain = [
        ['age_vehicle', '>', '1'],
        ['state', '!=', 'broken'],
    ];
    $order = 'model desc';
    $fields = ['model', 'date_purchased', 'garage_id', 'age_vehicle'];



    //Appel de méthode execute_kw et affichage du résultat
    //Cette version utilise l'argument load et donc le nom du garage n'est pas chargé
    $keyword_argument = ['order' => $order, 'domain' => $domain, 'fields' => $fields, "load" => "None"];

    //Cette version n'utilise pas l'argument load et donc le nom du garage est récupéré
    //$keyword_argument = ['order' => $order, 'domain' => $domain, 'fields' => $fields ];
    $positionnal_argument = [];

    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'search_read', $positionnal_argument, $keyword_argument);
    echo "<pre> " . print_r($donneesrecues, true) . "</pre>";

}

function create($object, $uid, $db, $cleapi)
{
    //première voiture 
    $imagePath = "photos/toyota.jpg";
    $imageData = file_get_contents($imagePath);
    $base64Image = base64_encode($imageData);

    $vehicule1 = [
        'model' => 'voiture API1',
        "date_purchased" => '2021-07-20',
        'immatriculation' => 'GX841DD',
        'garage_id' => 1,
        'state' => 'usable',
        'thumbnail' => $base64Image,
        'option_ids' => [1, 2]
    ];

    //deuxième voiture
    $imagePath = "photos/ford.jpg";
    $imageData = file_get_contents($imagePath);
    $base64Image = base64_encode($imageData);

    $vehicule2 = [
        'model' => 'voiture API2',
        "date_purchased" => '2021-07-21',
        'immatriculation' => 'GH841DD',
        'garage_id' => 1,
        'state' => 'usable',
        'thumbnail' => $base64Image,
        'option_ids' => []
    ];

    //Création du tableau d'enregistrement
    $vals_list = [$vehicule1, $vehicule2];


    //Création du tableau des arguments positionnels
    $positionnal_argument = [
        $vals_list
    ];


    //Envoi des données et affichage.
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'create', $positionnal_argument);
    echo "<pre>" . print_r($donneesrecues, true) . "</pre>";
}

function write($object, $uid, $cleapi, $db)
{
    //modification d'un élément
    $vehicule_id_a_modifier = [5];

    $data = [
        'model' => 'voiture modifiée par l\'API',
        'date_purchased' => '2021-07-15',
        'immatriculation' => 'VV000VV',
        'garage_id' => 2,
        'state' => 'broken',
    ];

    $positionnal_argument = [
        $vehicule_id_a_modifier,
        $data
    ];

    //Envoi des données et affichage.
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'write', $positionnal_argument);

    echo "<pre>" . print_r($donneesrecues, true) . "</pre>";

    // Modification de plusieurs éléments
    $vehicule_id_a_modifier = [1, 2, 5];
    $data = [
        'garage_id' => 2,
        'state' => 'usable'
    ];

    $positionnal_argument = [
        $vehicule_id_a_modifier,
        $data
    ];
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'write', $positionnal_argument);


    //Envoi des données et affichage.
    echo "<pre>" . print_r($donneesrecues, true) . "</pre>";
}

function unlike($db,$uid,$cleapi,$object) {
    //suppression d'un élément
    $vehicule_id_a_supprimer=[17];

    $positionnal_argument = [
        $vehicule_id_a_supprimer
    ];

    //envoi des données et affichage
    $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'unlink', $positionnal_argument);


        echo "<pre>" . print_r($donneesrecues, true) . "</pre>";      
       
        // Suppression de plusieurs éléments
        $vehicule_id_a_modifier=[18,19];     


        $positionnal_argument=[
            $vehicule_id_a_modifier,
        ];


        $donneesrecues = $object->execute_kw($db, $uid, $cleapi, 'rentcars.vehicle', 'unlink', $positionnal_argument);


        //Envoi des données et affichage.
        echo "<pre>" . print_r($donneesrecues, true) . "</pre>";
}





?>