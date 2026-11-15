import { compareDelivery } from "./dashboard.js";

export function renderDeliveryPanel(delivered: number, attempted: number, prior: number): string {
  const trend = compareDelivery(delivered, attempted, prior);
  return "Delivered shipments: " + trend;
}
