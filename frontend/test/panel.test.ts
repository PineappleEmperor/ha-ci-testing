import { describe, expect, it } from "vitest";

import { widthLabel } from "../src/ha-ci-demo-panel";

describe("widthLabel", () => {
  it("names the layout the panel renders", () => {
    expect(widthLabel(true)).toBe("narrow");
    expect(widthLabel(false)).toBe("wide");
  });
});
