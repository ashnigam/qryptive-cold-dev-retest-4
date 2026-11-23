import { createHash, generateKeyPairSync, createECDH, sign } from "crypto";

export function checksum(data: string): string {
  return createHash("md5").update(data).digest("hex");
}

export function signToken(data: Buffer): Buffer {
  const { privateKey } = generateKeyPairSync("rsa", { modulusLength: 2048 });
  return sign("sha256", data, privateKey);
}

export function sharedSecret(peer: Buffer): Buffer {
  const ecdh = createECDH("prime256v1");
  ecdh.generateKeys();
  return ecdh.computeSecret(peer);
}
