import { compareDelivery } from "./dashboard.js";
import { renderDeliveryPanel } from "./panel.js";

export function checkDeliveryComparison(): void {
  if (renderDeliveryPanel(0, 0, 0) !== "Delivered shipments: 0% flat") {
    throw new Error("empty delivery window must display zero");
  }
  if (compareDelivery(4, 5, 0.5) !== "80% up") throw new Error("unexpected trend");
  if (renderDeliveryPanel(1, 2, 0.5) !== "Delivered shipments: 50% flat") {
    throw new Error("unexpected label");
  }
}
