#!/usr/bin/env python3
"""Check the current Ethereum gas price from a public JSON-RPC endpoint."""

import json
import sys
import urllib.request

RPC_URL = "https://eth.llamarpc.com"


def rpc_call(method: str) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": []}).encode()
    req = urllib.request.Request(RPC_URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def main() -> int:
    try:
        gas = rpc_call("eth_gasPrice")
        block = rpc_call("eth_blockNumber")
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    gwei = int(gas["result"], 16) / 1e9
    number = int(block["result"], 16)
    print(f"gas price : {gwei:.1f} gwei")
    print(f"block     : {number:,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
