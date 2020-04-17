package exchanges.factories;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import org.knowm.xchange.currency.CurrencyPair;
import org.zeromq.ZContext;

import exchanges.factories.EntryPoint.Exchanges;
import utils.Config;
import utils.Constants;
import utils.CurrencyPairs;

public class {{Name}}Factory extends GenericFactory {

	{{Name}}Factory() {
		exchange = Exchanges.{{NAME}};
		ticker_pub = "{{NAME}}_TICKER_PUB";
		orderbook_pub = "{{NAME}}_ORDERBOOK_PUB";
	}

	public static void {{name}}(Boolean _listCmd, EntryPoint _ep, Set<CurrencyPair> _cp, ArrayList<Thread> _thds,
	        ZContext _ctx) throws IOException {
		if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_enabled))) {
			if (_listCmd) {
				CurrencyPairs.displayCurrencyPairs(Exchanges.{{NAME}}, _ep.getExchange(Exchanges.{{NAME}}).getCurrencyPairs());
			} else {
				Set<CurrencyPair> {{Name}}_cp = _cp;
				String bscp = Config.getInstance().get(Constants.{{name}}_currency_pairs);
				if (bscp != null && !bscp.isEmpty()) {
					{{Name}}_cp = new HashSet<>();
					for (String pair : bscp.split(",")) {
						{{Name}}_cp.add(new CurrencyPair(pair));
					}
				} else {
					{{Name}}_cp = _ep.getExchange(Exchanges.{{NAME}}).getCurrencyPairs();
					Iterator<CurrencyPair> pair = _cp.iterator();
					while (pair.hasNext()) {
						CurrencyPair p = pair.next();
						if (!{{Name}}_cp.contains(p)) {
							pair.remove();
						}
					}
				}

				// Set refresh time
				String refresh_timer = Config.getInstance().get(Constants.{{name}}_refresh_rate);
                if (refresh_timer != null) {
					ExchangesFactory.get{{Name}}Factory().setRefreshRate(Long.parseLong(refresh_timer) * 1000);
				}

				// Create a ticker from {{Name}}
				if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_ticker_enabled))) {
					_thds.addAll(ExchangesFactory.get{{Name}}Factory().create_ticker_feeders(_ep, _ctx, _cp));
				}

				// Create an orderbook from {{Name}}
				if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_orderbook_enabled))) {
					_thds.addAll(ExchangesFactory.get{{Name}}Factory().create_orderbook_feeders(_ep, _ctx, _cp));
				}
			}
		}
	}
}