package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Bienvenido a la tabla de multiplicar")
	var numtoMulti int64
	flag.Int64Var(&numtoMulti, "num", 0, "Coloca un numero para poder multiplicarlo hasta el 12")
	flag.Parse()
	if numtoMulti != 0 {
		var i int64 = 0
		for i < 13 {
			fmt.Println("El número es: ", &numtoMulti)
			fmt.Println("La tabla de multiplicar es: ")
			fmt.Println(numtoMulti * i)
			i++
		}
	} else {
		fmt.Println("El valor no puede ser 0")
		os.Exit(1)
	}
}
