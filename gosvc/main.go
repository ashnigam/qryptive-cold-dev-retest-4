package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/tls"
	"fmt"
)

func main() {
	key, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	h := sha256.Sum256([]byte("hello"))
	sig, _ := ecdsa.SignASN1(rand.Reader, key, h[:])
	fmt.Println(len(sig), sha1.Sum([]byte("legacy")))
	cfg := &tls.Config{MinVersion: tls.VersionTLS10}
	_ = cfg
}
