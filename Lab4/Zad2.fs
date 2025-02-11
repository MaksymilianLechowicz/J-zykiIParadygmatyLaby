let USD:float = 4.0
let PLN:float = 1.0
let GBR:float = 5.0
let EU:float = 4.0

let changetoOtherVal amount currency another:float=
    let mutable changetoPLN:float = 0
    if currency = 1.0 then changetoPLN <- amount
    elif currency = 4.0 then changetoPLN <- amount*4.0
    elif currency = 5.0 then changetoPLN <- amount*5.0

    if another = 1.0 then changetoPLN <- amount
    elif another = 4.0 then changetoPLN <- changetoPLN/4.0
    elif another = 5.0 then changetoPLN <- changetoPLN/5.0

    changetoPLN


let calculate = changetoOtherVal 100 GBR EU
let calculate2 = changetoOtherVal 200 PLN GBR
printf "Twoja kwota wynosi: %.2f" calculate
printfn " po konwersji"
printf "Twoja kwota wynosi: %.2f" calculate2
printf " po konwersji"