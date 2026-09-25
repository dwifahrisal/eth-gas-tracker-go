# eth-gas-tracker

A tiny CLI that reports the current Ethereum gas price and latest block number, using a public JSON-RPC endpoint. No external dependencies.

## Usage

```bash
python3 gas.py
```

Example output:

```
gas price : 12.3 gwei
block     : 21,345,678
```

## Notes

- Uses `eth.llamarpc.com` by default; swap `RPC_URL` to point at another public endpoint.
- The public RPC is rate limited — fine for occasional checks.
- Works with Python 3.8+.
