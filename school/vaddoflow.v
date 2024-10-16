module vaddoflow (
  input [3:0] a, b,
  output [6:0] segL,
  output oflow
);
  wire [4:0] x;

  assign x = a + b;
  assign segL[3:0] = x[3:0];
  assign oflow = x[4];

endmodule