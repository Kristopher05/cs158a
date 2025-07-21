This code replicates the leader election algorithm by using asynchronous rings that run in O(n^2) time. The sending direction is based on the client-server relationship and once the client is connected to a server it sends a message with their uuid once. They are connected by editing the config file port numbers, which will need to be edited before running each process.

First node:

Second node:

Third node: