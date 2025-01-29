module Zad2

open System
open System.IO

let sprPalindrom(str:string) =
    let clearText = str.Replace(" ", "").ToLower()
    clearText = string(Array.rev(clearText.ToCharArray()))

printfn "Podaj text: "
let inputText = Console.ReadLine()

if sprPalindrom inputText then
    printfn "Podany text jest palindromem"
else
    printfn "Podany text nie jest palindromem"
