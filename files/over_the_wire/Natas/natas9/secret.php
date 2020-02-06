<? php 
    $hextext = "3d3d516343746d4d6d6c315669563362";
    $secret = base64_decode(strrev(hex2bin($hextext)));
    function console_log( $data ){
        echo '<script>';
        echo 'console.log('. json_encode( $data ) .')';
        echo '</script>';
      }
      console_log($secret);
?>      