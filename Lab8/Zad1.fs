open System
open System.Collections.Generic

type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

//let Head = 
//    function
//    | Empty -> failwith "Lista pusta."
//    | Node(Head,_) ->Head

//let Tail =
//    function
//    | Empty -> failwith "Lista pusta"
//    | Node(Tail,_) -> Tail

//let addHead value list =
//    Node(value,list)

//let rec pristList list =
//    match list with
//    | Empty -> ()
//    | Node (value, next) ->
//        printf "%A" value
//        pristList next

//[<EntryPoint>]
//let main argv =
//    let list1 = Empty

//    pristList list1
//    let list2 = addHead 1 list1
//    let list2 = addHead 2 list2

//    0


let rec fromList = 
    function
        | [] -> Empty
        | x::xs ->Node(x,fromList xs)
