<html>
  <head>
    <title>This is Homepage</title>
  <style>
  body {
background-color: rgb(114, 169, 187);
}

h1 {
color: white;
text-align: center;
}

p {
font-family: verdana;
font-size: 20px;
}
</style>
</head>

  <body>
  
    <h1>Twitter Botcheck & Sentiment Analysis Tool.</h1>
    <form  method="POST" name="user_sentiment">
        {% if error %}
        <p> Invalid. Please enter in a twitter user. </p>
        {% endif %}
        </p>           
        <p><b> Please enter a twitter user ID (include @): </b></p>
        <p>
        <input type="text" size="18" name="account" placeholder="Ex: @janedoe">
        </p>
        <p><b> How many tweets (keep between 1-200 results per API limits): </b></p>
        <p>
        <input type="text" size="18" name="count" value=50>
        </p>
        <br>
            <input type="submit" value="Magic Happens" /> 
        </br>

    </form>
  </body>

</html>