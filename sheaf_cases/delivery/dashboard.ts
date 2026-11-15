import { deliveryRate } from "./rate.js";

export function compareDelivery(current: number, attempted: number, prior: number): string {
  const rate = deliveryRate(current, attempted);
  const difference = rate - prior;
  const percent = Math.round(rate * 100);
  const trend = difference > 0 ? "up" : difference < 0 ? "down" : "flat";
  return percent + "% " + trend;
}
