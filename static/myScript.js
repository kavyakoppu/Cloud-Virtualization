$('#submit').click(function(){
    const number = $('#number').val();
    if(number!==undefined || number !== null){
        // $.ajax({
        //     url: "http://18.222.125.227/isPrime",
        //     data: {'number': number}
        //   }).done(onSuccessCallThis);
        $.post('http://18.222.125.227/isPrime', {'number': number}, function(data){
            console.log(data);
            isPrime = data['isPrime']
            const num = data['number'];
            console.log(isPrime);
            if(isPrime===true){
                $('#output').html(num+' is a prime number!');
            }else{
                $('#output').html(num+' is not a prime number!');
            }
        });
    }
})





