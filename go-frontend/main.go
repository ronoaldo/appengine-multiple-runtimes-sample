package app

import (
	"fmt"
	"net/http"
)

func init() {
	http.HandleFunc("/", Hello)
}

func Hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, world from Go")
}
