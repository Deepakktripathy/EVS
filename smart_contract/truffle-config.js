// require("dotenv").config();
const HDWalletProvider = require("@truffle/hdwallet-provider");

const privateKey = "0x68d00c9d00826eef79b30dd53c8fc1c8d7894c7ce6dd56ac6f6d7de51503fbf1";
const alchemy_api_key = "XCkiGkTXVL1_H74OJ3zs0GLriRvoRYeQ";

module.exports = {
  plugins: ["truffle-plugin-verify"],
  networks: {
    goerli: {
      provider: () =>
        new HDWalletProvider(
          privateKey,
          `https://eth-goerli.g.alchemy.com/v2/${alchemy_api_key}`
        ),
      network_id: 5,
      confirmations: 1,
      timeoutBlocks: 200,
      skipDryRun: true,
    },
  },
  mocha: {},

  compilers: {
    solc: {
      version: "^0.8.16",
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
        evmVersion: "byzantium",
      },
    },
  },
  db: {
    enabled: false,
  },
};

//0xed2276423d3fDfebd5e25F76Ab95e685901F73d1