// For more information see https://aka.ms/fsharp-console-apps

open System
//let str1 ="Witaj"
//let str2 = "F3"

//let str3 = str1 + " w " + str2

//printf "%s" str3

//let str4 = "Witaj,w,F#"

//let words = str4.Split([|',';';';':';' '|], System.StringSplitOptions.RemoveEmptyEntries);
//printfn "%A" words

//let joined = String.Join(" - ", words)

//printf "%s" joined



open System.Text.RegularExpressions
open System.IO

//let regex = Regex(@"\d") // \d - 0 - 9; co najmniej jedno wystąpienie lub więcej
//let isMatch = regex.IsMatch("test123")
//printfn "%b" isMatch

//let multiline = @"to jest
//wielowierszowy
//tekst"

//printfn "%s" multiline


//let filePath = "output.txt"
//let text = "to jest przykładowy tekst"

//File.WriteAllText(filePath,text)

//let lines = ["Linia 1";"Linia 2"; "Linia 3"]
//File.AppendAllText(filePath, text)
//File.AppendAllLines(filePath, lines)

//let readtext = File.ReadAllText(filePath)

//printfn "Zawartośc pliku: \n%s" readtext




let countWords(str:string) = 
    str.Split([|' ';'\t'; '\n';';';':';'.'|], StringSplitOptions.RemoveEmptyEntries)
    |>Array.length

let countLetters(str:string) =
    str.Replace(" ","").Length

printfn "Podaj text: "
let answer = Console.ReadLine()
let wordCount = countWords answer
let charCount = countLetters answer

printf "Liczba słów: %d Liczba znaków:  %d" wordCount charCount



