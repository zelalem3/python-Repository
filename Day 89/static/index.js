



    document.getElementById("text").addEventListener("keyup", event =>
    {
    const timeout = setTimeout(function clearfunction()
    {
//    document,getElementById("text").classList.add("added-class");
    document.getElementById("text").value = " "
    }, 10000)


    });

    document.getElementById("text").addEventListener("keydown", event =>
    {
        clearTimeout(timeout)
    });


