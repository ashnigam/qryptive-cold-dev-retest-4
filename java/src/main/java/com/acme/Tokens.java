package com.acme;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.Signature;
import javax.crypto.Cipher;
import javax.crypto.KeyAgreement;

public class Tokens {
    public byte[] sign(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair kp = kpg.generateKeyPair();
        Signature s = Signature.getInstance("SHA256withRSA");
        s.initSign(kp.getPrivate());
        s.update(data);
        return s.sign();
    }

    public byte[] digest(byte[] data) throws Exception {
        return MessageDigest.getInstance("MD5").digest(data);
    }

    public Cipher legacyCipher() throws Exception {
        return Cipher.getInstance("DES/ECB/PKCS5Padding");
    }

    public KeyAgreement agreement() throws Exception {
        return KeyAgreement.getInstance("ECDH");
    }
}
